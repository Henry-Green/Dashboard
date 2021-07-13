// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: partner_api.proto

package com.emporiaenergy.protos.partnerapi;

/**
 * Protobuf enum {@code protos.ResultStatus}
 */
public enum ResultStatus
    implements com.google.protobuf.ProtocolMessageEnum {
  /**
   * <code>VALID = 0;</code>
   */
  VALID(0),
  /**
   * <code>AUTH_INVALID_CREDENTIALS = 1;</code>
   */
  AUTH_INVALID_CREDENTIALS(1),
  /**
   * <code>AUTH_INVALID_TOKEN = 2;</code>
   */
  AUTH_INVALID_TOKEN(2),
  /**
   * <code>AUTH_EXPIRED = 3;</code>
   */
  AUTH_EXPIRED(3),
  /**
   * <code>INVALID_USAGE_SCALE = 4;</code>
   */
  INVALID_USAGE_SCALE(4),
  /**
   * <code>INTERNAL_ERROR = 100;</code>
   */
  INTERNAL_ERROR(100),
  UNRECOGNIZED(-1),
  ;

  /**
   * <code>VALID = 0;</code>
   */
  public static final int VALID_VALUE = 0;
  /**
   * <code>AUTH_INVALID_CREDENTIALS = 1;</code>
   */
  public static final int AUTH_INVALID_CREDENTIALS_VALUE = 1;
  /**
   * <code>AUTH_INVALID_TOKEN = 2;</code>
   */
  public static final int AUTH_INVALID_TOKEN_VALUE = 2;
  /**
   * <code>AUTH_EXPIRED = 3;</code>
   */
  public static final int AUTH_EXPIRED_VALUE = 3;
  /**
   * <code>INVALID_USAGE_SCALE = 4;</code>
   */
  public static final int INVALID_USAGE_SCALE_VALUE = 4;
  /**
   * <code>INTERNAL_ERROR = 100;</code>
   */
  public static final int INTERNAL_ERROR_VALUE = 100;


  public final int getNumber() {
    if (this == UNRECOGNIZED) {
      throw new java.lang.IllegalArgumentException(
          "Can't get the number of an unknown enum value.");
    }
    return value;
  }

  /**
   * @param value The numeric wire value of the corresponding enum entry.
   * @return The enum associated with the given numeric wire value.
   * @deprecated Use {@link #forNumber(int)} instead.
   */
  @java.lang.Deprecated
  public static ResultStatus valueOf(int value) {
    return forNumber(value);
  }

  /**
   * @param value The numeric wire value of the corresponding enum entry.
   * @return The enum associated with the given numeric wire value.
   */
  public static ResultStatus forNumber(int value) {
    switch (value) {
      case 0: return VALID;
      case 1: return AUTH_INVALID_CREDENTIALS;
      case 2: return AUTH_INVALID_TOKEN;
      case 3: return AUTH_EXPIRED;
      case 4: return INVALID_USAGE_SCALE;
      case 100: return INTERNAL_ERROR;
      default: return null;
    }
  }

  public static com.google.protobuf.Internal.EnumLiteMap<ResultStatus>
      internalGetValueMap() {
    return internalValueMap;
  }
  private static final com.google.protobuf.Internal.EnumLiteMap<
      ResultStatus> internalValueMap =
        new com.google.protobuf.Internal.EnumLiteMap<ResultStatus>() {
          public ResultStatus findValueByNumber(int number) {
            return ResultStatus.forNumber(number);
          }
        };

  public final com.google.protobuf.Descriptors.EnumValueDescriptor
      getValueDescriptor() {
    if (this == UNRECOGNIZED) {
      throw new java.lang.IllegalStateException(
          "Can't get the descriptor of an unrecognized enum value.");
    }
    return getDescriptor().getValues().get(ordinal());
  }
  public final com.google.protobuf.Descriptors.EnumDescriptor
      getDescriptorForType() {
    return getDescriptor();
  }
  public static final com.google.protobuf.Descriptors.EnumDescriptor
      getDescriptor() {
    return com.emporiaenergy.protos.partnerapi.PartnerApiProto.getDescriptor().getEnumTypes().get(0);
  }

  private static final ResultStatus[] VALUES = values();

  public static ResultStatus valueOf(
      com.google.protobuf.Descriptors.EnumValueDescriptor desc) {
    if (desc.getType() != getDescriptor()) {
      throw new java.lang.IllegalArgumentException(
        "EnumValueDescriptor is not for this type.");
    }
    if (desc.getIndex() == -1) {
      return UNRECOGNIZED;
    }
    return VALUES[desc.getIndex()];
  }

  private final int value;

  private ResultStatus(int value) {
    this.value = value;
  }

  // @@protoc_insertion_point(enum_scope:protos.ResultStatus)
}

